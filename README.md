# Efficient-LLM-Supervised-Fine-Tuning
Efficient LLM Supervised Fine Tuning

### Motivation

#### What problem does this project try to solve?
Large language models (LLMs) are adept at knowledge extraction and reasoning, particularly through in-context learning. The challenge lies in the extensive memory requirements due to long context consumption by example question-answer pairs. This project seeks to explore alternatives to the standard approach of training models from scratch for long-context windows.

### Problem Statement
Identify the most efficient method for learning from multiple example prompts followed by a question.

### Approaches
- **Comparison**: Few-shot fine-tuning versus in-context learning, with prior findings suggesting comparable results between the two ([Research Comparison](https://aclanthology.org/2023.findings-acl.779.pdf)).
- **Innovative Method**: "Context Distillation" as proposed by Anthropic, focusing on fine-tuning based on KL divergence to minimize overfitting on small datasets ([Context Distillation Paper](https://arxiv.org/abs/2112.00861)).
- **Application**: Implementing the context-distillation method for the NLI classification task, compared against in-context learning.

### Benchmarks
- **Datasets**: Open-source benchmarks available on [GitHub](https://github.com/uds-lsv/llmft).
- **Models**: Range from OPT-125M to OPT-30B, depending on available compute resources.
- **Metrics**: Compare in-domain and out-of-domain accuracy, alongside system resource requirements.

### Scope
- **Goal**: Implement alternative fine-tuning approaches, such as context-distillation or other proposed methods.
- **Fine-tuning Techniques**:
  - Vanilla fine-tuning with a new classification head.
  - Pattern-based fine-tuning using the pre-trained language modeling head.
  - Parameter-efficient methods like BitFit and LoRA adapters.
- **Difficulty**: Medium, suitable for a team of 3-4 people.
