from sentence_transformers import SentenceTransformer, util
import logging

logging.basicConfig(
    level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(module)s - %(message)s"
)
logger = logging.getLogger(__name__)


class GPT2CosineSimilarity:
    def __init__(self, model_name="all-MiniLM-L6-v2"):
        self.model = SentenceTransformer(model_name)
        logger.info(f"DOWNLOADED {model_name}")

    def get_cosine_similarity(self, text1, text2):
        # generate text embeddings
        embeddings1 = self.model.encode(text1)
        embeddings2 = self.model.encode(text2)

        # compute cosine score
        cosine_score = util.cos_sim(
            embeddings1, embeddings2
        ).item()  # item() - converts the single tensor to python number

        return round(cosine_score, 3)


# import torch
# from transformers import GPT2Tokenizer, GPT2Model


# class GPT2CosineSimilarity:
#     def __init__(self):
#         self.tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
#         self.model = GPT2Model.from_pretrained("gpt2")

#     def get_cosine_similarity(self, text1, text2):
#         # Tokenize the input texts
#         tokens1 = self.tokenizer.encode(text1, add_special_tokens=True)
#         tokens2 = self.tokenizer.encode(text2, add_special_tokens=True)

#         # Convert the tokens to PyTorch tensors
#         input_ids1 = torch.tensor(tokens1).unsqueeze(0)  # Batch size 1
#         input_ids2 = torch.tensor(tokens2).unsqueeze(0)  # Batch size 1

#         # Generate the embeddings for the input texts using the GPT-2 model
#         with torch.no_grad():
#             embeddings1 = self.model(input_ids1)[0][
#                 :, 0, :
#             ]  # Take the first (CLS) token's embedding
#             embeddings2 = self.model(input_ids2)[0][
#                 :, 0, :
#             ]  # Take the first (CLS) token's embedding

#         # Calculate the cosine similarity between the embeddings of the two input texts
#         similarity = torch.nn.functional.cosine_similarity(embeddings1, embeddings2)

#         return similarity.item()
