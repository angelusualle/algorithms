from collections import defaultdict

def sparse_similarity(doc_words):
    word_doc = defaultdict(set)
    for k in doc_words:
        for w in doc_words[k]:
            word_doc[w].add(k)
    doc_sim = []
    for k in doc_words:
        docs = set()
        for w in doc_words[k]:
            for d in word_doc[w]:
                if d != k:
                    docs.add(d)
        for d in docs:
            sim = len(doc_words[k].intersection(doc_words[d])) / len(doc_words[k].union(doc_words[d]))
            doc_sim.append('%s to %s : %f' % (k, d, sim))
    return doc_sim
        
