#!/usr/bin/env python
# coding: utf-8

# In[23]:


import jieba
import jieba.posseg as pseg
print ("加載用戶詞典 ......")

jieba.load_userdict('data/pos.txt')
jieba.load_userdict('data/neg.txt')


# In[24]:


# 分詞，返回List
def segmentation(sentence):
    seg_list = jieba.cut(sentence)
    seg_result = []
    for w in seg_list:
        seg_result.append(w)
    #print seg_result[:]
    return seg_result


# In[25]:


# 分詞，詞性標註，詞和詞性構成一個元組
def postagger(sentence):
    pos_data = pseg.cut(sentence)
    pos_list = []
    for w in pos_data:
        pos_list.append((w.word, w.flag))
    #print pos_list[:]
    return pos_list


# In[26]:


# 句子切分
def cut_sentence(words):
    start = 0
    i = 0
    token = 'meaningless'
    sents = []
    punt_list = ',.!?;~，。！？；～… '
    #print "punc_list", punt_list
    for word in words:
        #print "word", word
        if word not in punt_list:   # 如果不是標點符號
            #print "word1", word
            i += 1
            token = list(words[start:i+2]).pop()
            #print "token:", token
        elif word in punt_list and token in punt_list:  # 處理省略號
            #print "word2", word
            i += 1
            token = list(words[start:i+2]).pop()
            #print "token:", token
        else:
            #print "word3", word
            sents.append(words[start:i+1])   # 斷句
            start = i + 1
            i += 1
    if start < len(words):   # 處理最後的部分
        sents.append(words[start:])
    return sents


# In[27]:


def read_lines(filename):
    fp = open(filename, 'r')
    lines = []
    for line in fp.readlines():
        line = line.strip()
        lines.append(line)
    fp.close()
    return lines


# In[28]:


# 去除停用詞
def del_stopwords(seg_sent):
    stopwords = read_lines("data/stop_words.txt")  # 讀取停用詞表
    new_sent = []   # 去除停用詞後的句子
    for word in seg_sent:
        if word in stopwords:
            continue
        else:
            new_sent.append(word)
    return new_sent


# In[29]:


# 獲取六種權值的詞，根據要求返回list
def read_quanzhi(request):
    result_dict = []
    if request == "one":
        result_dict = read_lines("data/most.txt")
    elif request == "two":
        result_dict = read_lines("data/very.txt")
    elif request == "three":
        result_dict = read_lines("data/more.txt")
    elif request == "four":
        result_dict = read_lines("data/ish.txt")
    elif request == "five":
        result_dict = read_lines("data/insufficiently.txt")
    elif request == "six":
        result_dict = read_lines("data/inverse.txt")
    else:
        pass
    return result_dict


# In[30]:


#if __name__ == '__main__':
#    test_sentence1 = "你地客服可唔可以專業D，問非所答，答非所問"


# In[31]:


#print (postagger(test_sentence1))


# In[32]:


#print (cut_sentence(test_sentence1))


# In[ ]:




