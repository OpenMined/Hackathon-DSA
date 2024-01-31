from rouge_score import rouge_scorer

def eval_rouge(answers, train_answers, train_context):
    # We can change what Rouge Score we want here:
    scorer = rouge_scorer.RougeScorer(['rougeL'], use_stemmer=True)

    ref_score = 0
    total_rouge_score = 0
    for answer in answers:
        idx = answers.index(answer)
        ref_answer = train_answers[idx][0]
        ref_context = train_context[idx]
        
        context_links = []
        for context_source in answer['source_documents']:
            context_file = context_source['source']
            with open(context_file) as f:
                context_link = f.readline()[16:-1]
            context_links.append(context_link)
        
        if context_links[0] == ref_context:
            ref_score += 1
        
        rouge_score = scorer.score(answer['content'], ref_answer)
        total_rouge_score += rouge_score["rougeL"].fmeasure
    return total_rouge_score/len(answers), ref_score/len(answers)