import json
from sentence_transformers import SentenceTransformer, CrossEncoder, util
import gzip
import os
import torch
import pandas as pd

df = pd.read_json('product_title.json' , lines=True)
df.head()

if not torch.cuda.is_available():
    print("Warning: No GPU found. Please add GPU to your notebook")

#We use the Bi-Encoder to encode all passages, so that we can use it with sematic search
bi_encoder = SentenceTransformer('multi-qa-MiniLM-L6-cos-v1')
bi_encoder.max_seq_length = 256     #Truncate long passages to 256 tokens
top_k = 32                          #Number of passages we want to retrieve with the bi-encoder

#The bi-encoder will retrieve 100 documents. We use a cross-encoder, to re-rank the results list to improve the quality

# We encode all passages into our vector space. This takes about 5 minutes (depends on your GPU speed)
#corpus_embeddings = bi_encoder.encode(df['text'], convert_to_tensor=True, show_progress_bar=True)

# We lower case our text and remove stop-words from indexing
def bm25_tokenizer(text):
    tokenized_doc = []
    for token in text.lower().split():
        token = token.strip(string.punctuation)

        if len(token) > 0 and token not in _stop_words.ENGLISH_STOP_WORDS:
            tokenized_doc.append(token)
    return tokenized_doc


corpus_embeddings = torch.load("embeddings.pt",map_location=torch.device('cpu') )


# This function will search all wikipedia articles for passages that
# answer the query
def search(query):
    print("Input question:", query)

    ##### Sematic Search #####
    # Encode the query using the bi-encoder and find potentially relevant passages
    question_embedding = bi_encoder.encode(query, convert_to_tensor=True)
    #question_embedding = question_embedding.cuda()
    hits = util.semantic_search(question_embedding, corpus_embeddings, top_k=top_k)
    hits = hits[0]  # Get the hits for the first query
    print(hits)
    ##### Re-Ranking #####
    # Now, score all retrieved passages with the cross_encoder
    cross_inp = [[query, df['id'][hit['corpus_id']]] for hit in hits]
    cross_scores = cross_encoder.predict(cross_inp)

    # Sort results by the cross-encoder scores
    for idx in range(len(cross_scores)):
        hits[idx]['cross-score'] = cross_scores[idx]


    # Output of top-5 hits from re-ranker
    print("\n-------------------------\n")
    print("Top-10 Cross-Encoder Re-ranker hits")
    hits = sorted(hits, key=lambda x: x['cross-score'], reverse=True)
    final_df = []
    
    for hit in hits[0:10]:
        
        id_var = df['id'][hit['corpus_id']].replace("\n", " ")
        test_var = df['text'][hit['corpus_id']].replace("\n", " ")
        score = hit['cross-score']
        d={'id_var':id_var,'text':test_var,'Score':score}
        df_final_new =pd.DataFrame(d,index=[0])
        final_df.append(df_final_new)
        #print("\t{}\t{}\t{:.3f}".format(df['id'][hit['corpus_id']].replace("\n", " "),df['text'][hit['corpus_id']].replace("\n", " "),hit['cross-score']))

    final_df=pd.concat(final_df)
    
    return final_df



