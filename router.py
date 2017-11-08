from flask import jsonify
from newspaper import Article
import json
import base64
import re

def ping():
    """Network Ping Test
    """
    return json.dumps({'Hello':'World'})

def extractBodyHtml(url, language='zh'):
    """抽取指定Body Html编码, URL是经过Base64编码之后的字符串
    """
    result={}
    try:
        u = (base64.b64decode(url)).decode("utf-8") 
        article = Article(u,language=language, keep_article_html=True)
        article.download()
        article.parse()
        result['content']=article.article_html
        result['code']=200
    except:
        result['code']=500
        result['content']=""
    return json.dumps(result) 

def extractText(url, language='zh'):
    """抽取指定文字内容, URL是经过Base64编码之后的字符串
    """
    result={}
    try:
        u = (base64.b64decode(url)).decode("utf-8") 
        article = Article(u,language=language)
        article.download()
        article.parse()
        result['code']=200
        result['title']=article.title
        result['content']=article.text
    except:
        result['code']=500
        result['title']=""
        result['content']=""
    return json.dumps(result)  

def extractImg(url, language='zh'):
    """抽取指定图片内容, URL是经过Base64编码之后的字符串
    """
    result={}
    try:
        u = (base64.b64decode(url)).decode("utf-8") 
        article = Article(u,language=language, keep_article_html=True)
        article.download()
        article.parse()
        result['code']=200
        result['top']=article.top_image
        reg=r'src=\"(\S+)\"'
        imgs=re.findall(reg,article.article_html)
        result['images']=imgs
    except:
        result['code']=500
        result['top']=""
        result['images']=""
    return json.dumps(result)      

def extractAllInfo(url, language='zh'):
    """抽取指定URL所有信息,包括文字,HTML代码,图片信息, URL是经过Base64编码之后的字符串
    """
    result={}
    try:
        u = (base64.b64decode(url)).decode("utf-8") 
        article = Article(u,language=language, keep_article_html=True)
        article.download()
        article.parse()
        article.nlp()
        result['code']=200
        result['top']=article.top_image
        reg=r'src=\"(\S+)\"'
        imgs=re.findall(reg,article.article_html)
        result['images']=imgs
        result['title']=article.title
        result['bodyHtml']=article.article_html
        result['body']=article.text
        result['authors']=article.authors
        result['keywords']=article.keywords
        result['summary']=article.summary
    except:
        print("Unexpected error:", sys.exc_info()[0])
        result['code']=500
        result['top']=""
        result['images']=""
        result['title']=""
        result['bodyHtml']=""
        result['body']=""
        result['authors']=""
        result['keywords']=""
        result['summary']=""
    return json.dumps(result)       