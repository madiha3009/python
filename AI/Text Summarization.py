from nltk.tokenize import sent_tokenize
from collections import Counter
import spacy

nlp = spacy.load("en_core_web_sm")

def summarize(text, n=2):
    sentences = sent_tokenize(text)
    word_freq = Counter(text.split())
    scores = []
    for sentence in sentences:
        doc = nlp(sentence)
        score = sum(word_freq[word.text] for word in doc) / len(doc)
        scores.append((sentence, score))
    summary = sorted(scores, key=lambda x: x[1], reverse=True)[:n]
    return [sentence for sentence, score in summary]

text = """The Science and Technology section examines candidates on their awareness of recent advancements and their applications, It also includes topics related to historical scientific achievements, especially those relevant to India.
This section also tests knowledge of basic IT, space, computers, robotics, biotechnology, and issues related to intellectual property rights.
Science and Technology Important Topics for Prelims: Science and Technology has a vast syllabus in the UPSC syllabus, particularly in the Prelims exam.
Therefore, it is crucial for the candidates to scrutinise Science and technology important topics for UPSC prelims to prepare well for the exam and score higher marks.
This subject integrates crucial innovations, advancements, and scientific principles that influence both national and global landscapes. Grasping key topics in Science and Technology not only assists in the Prelims but also enriches the candidates’ knowledge base for the Mains and interview stages.
Here, we have provided a focused guide to help candidates prepare effectively for the Science and technology important topics for prelims 2024.
By focusing on these areas and following the preparation tips, candidates can effectively master the important Science and Technology topics for UPSC prelims 2024.
Consistent study and staying updated on scientific developments are crucial for success in this section.
This structured approach will help students tackle the Science and Technology section effectively, equipping them with the knowledge to answer both straightforward and application-based questions accurately.
To boost your preparation, consider enrolling in PW UPSC online coaching for expert guidance tailored to cover topics strictly as per the Prelims syllabus."""

summary = summarize(text)

for sentence in summary:
    print(sentence)

from collections import Counter
import nltk

def identify_topic(text):
    words = nltk.word_tokenize(text)
    stopwords = set(nltk.corpus.stopwords.words("english"))
    filtered_words = [word.lower() for word in words if word.isalnum() and word.lower() not in stopwords]
    word_freq = Counter(filtered_words)
    topic = " ".join(word for word, _ in word_freq.most_common(3))  # Adjust number of words as needed
    
    return topic


topic = identify_topic(text)
print("The topic of the text is:", topic)
