#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 13:57:20 2019

@author: moises
"""

#inclua aqui o caminho para o arquivo com o corpus LIMPO e TOKENIZADO
nome_arquivo_corpus = '   '

#inclua aqui o caminho para o arquivo com a lista de stopwords
nome_arquivo_stopwords = '   '

arq_corpus = open(nome_arquivo_corpus, 'r')
texto_corpus = arq_corpus.read().split()
arq_corpus.close()

arq_stopwords = open(nome_arquivo_stopwords, 'r')
texto_stopwords = arq_stopwords.read().split()
arq_stopwords.close()

texto_sem_stopwords = [termo for termo in texto_corpus if not termo in texto_stopwords]
print (texto_sem_stopwords)   

#construa a exportação para arquivo texto...
