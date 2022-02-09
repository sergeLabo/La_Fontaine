"""
Here's how you can quickly test out aitextgen on your own computer, even if you don't have a GPU!

Les téléchargements se font dans le dossier aitextgen

For generating text from a pretrained GPT-2 model:
"""
from aitextgen import aitextgen

# Without any parameters, aitextgen() will download, cache, and load
# the 124M GPT-2 "small" model
ai = aitextgen()

ai.generate()
ai.generate(n=3, max_length=100)
ai.generate(n=3, prompt="I believe in unicorns because", max_length=100)
ai.generate_to_file(n=10,
                    prompt="I believe in unicorns because",
                    max_length=100,
                    temperature=1.2)
