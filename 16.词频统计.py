#文本词频统计
#文本预处理：大小写，去掉符号,停用词
from random import sample


def preprocess_text(text):
    # 定义标点符号集合（需去除的字符）
    punctuation = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
    # 定义停用词（无实际意义的常用词）
    stop_words = {"a", "an", "the", "in", "on", "at", "of", "to", "for", "and", "but",
                  "or", "so", "am", "is", "are", "was", "were", "do", "does", "di",
                  "have", "has", "had", "it","i","you","my"}
    #大小写统一转小写
    text_lower = text.lower()
    #去除标点符号
    text_clean=text_lower.translate(str.maketrans('', '', punctuation))
    #拆分，过滤空字符串
    words=[word for word in text_clean.split() if word.strip()!=""]
    #过滤停用词
    filtered_words = [word for word in words if word not in stop_words]
    return filtered_words

def count_word_frequency(words):
    word_freq={}
    for word in words:
        word_freq[word] =word_freq.get(word,0)+1
    return word_freq

def analyze_text(text):
    #预处理文本
    words = preprocess_text(text)
    if not words:
        print("No words found")
        return
    #统计词频
    word_freq = count_word_frequency(words)
    #按词频降序排序（取前十）
    sorted_freq = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)[:10]
    #输出结果
    print("Top 10 words:")
    print("Word\t Frequency")
    print("------------------")
    for word, freq in sorted_freq:
        print(f"{word}: {freq}")
    return sorted_freq
"""
if __name__ == "__main__":
    with open("hamlet.txt", "r", encoding="utf-8") as file:
        text = file.read()
    analyze_text(text)
"""
sample_text=open("hamlet.txt","r",encoding="utf-8").read()
analyze_text(sample_text)


