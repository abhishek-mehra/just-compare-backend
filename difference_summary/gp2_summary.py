class GPT2Summary:
    def __init__(self):
        pass

    def generate_gp2_summary(self, text1, text2):
        return "Continous deployment from cloud build pass"


# from transformers import GPT2Tokenizer, GPT2LMHeadModel


# class GPT2Summary:
#     def __init__(self):
#         self.tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
#         self.model = GPT2LMHeadModel.from_pretrained("gpt2")

#     def generate_gp2_summary(self, text1, text2):
#         # Combine the two texts into a single input
#         input_text = f"{text1} {text2}"

#         # Tokenize the input text
#         input_ids = self.tokenizer.encode(input_text, return_tensors="pt")

#         # Generate a summary of the input text using the GPT-2 model
#         summary_ids = self.model.generate(input_ids, max_length=100, do_sample=True)

#         # Decode the summary output
#         summary = self.tokenizer.decode(summary_ids[0], skip_special_tokens=True)

#         return summary
