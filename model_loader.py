from transformers import AutoTokenizer, AutoModelForCausalLM


class ModelLoader:
    def __init__(self, model_name="facebook/opt-1.3b"):
        # Load the tokenizer
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)

        # Load the model
        self.model = AutoModelForCausalLM.from_pretrained(model_name)

    def generate_text(self, input_text):
        # Tokenize the input text
        input_ids = self.tokenizer(input_text, return_tensors='pt').input_ids

        # Generate text using the model
        output = self.model.generate(input_ids, max_length=50)

        # Decode the generated text
        output_text = self.tokenizer.decode(output[0], skip_special_tokens=True)

        return output_text


if __name__ == "__main__":
    cur_model = ModelLoader()
    print(cur_model.generate_text("Once upon a time"))
