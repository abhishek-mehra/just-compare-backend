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


class GPT2CosineSimilarity:
    def __init__(self):
        pass

    def get_cosine_similarity(self, text1, text2):
        return "similarity generated"
