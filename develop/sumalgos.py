from sumy.summarizers.lex_rank import LexRankSummarizer
from sumy.summarizers.lsa import LsaSummarizer
from sumy.summarizers.luhn import LuhnSummarizer 
from sumy.summarizers.text_rank import TextRankSummarizer
from sumy.summarizers.kl import KLSummarizer
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.stemmers import Stemmer
from sumy.utils import get_stop_words
from develop.sumeval import *

def summarize(doc, summarizer):
	summary = summarizer(doc.document, '20%')
	return summary

def lsa(doc, refsum, debug = False):
	stemmer = Stemmer("english")
	summarizer = LsaSummarizer(stemmer)
	summarizer.stop_words = get_stop_words("english")
	summary = summarize(doc, summarizer)
	return evaluate(summary, refsum, debug=True)

def lexrank(doc, refsum):
	stemmer = Stemmer("english")
	summarizer = LexRankSummarizer(stemmer)
	summarizer.stop_words = get_stop_words("english")
	summary = summarize(doc, summarizer)
	return evaluate(summary, refsum)

def textrank(doc, refsum):
	stemmer = Stemmer("english")
	summarizer = TextRankSummarizer(stemmer)
	summarizer.stop_words = get_stop_words("english")
	summary = summarize(doc, summarizer)
	return evaluate(summary, refsum)

def luhn(doc, refsum):
	stemmer = Stemmer("english")
	summarizer = LuhnSummarizer(stemmer)
	summarizer.stop_words = get_stop_words("english")
	summary = summarize(doc, summarizer)
	return evaluate(summary, refsum)

def klsum(doc, refsum):
	stemmer = Stemmer("english")
	summarizer = KLSummarizer(stemmer)
	summarizer.stop_words = get_stop_words("english")
	summary = summarize(doc, summarizer)
	return evaluate(summary, refsum)
def lexrankk(doc):
	stemmer = Stemmer("english")
	summarizer = LexRankSummarizer(stemmer)
	summarizer.stop_words = get_stop_words("english")
	summary = summarize(doc, summarizer)
	return summary

def textrankk(doc):
	stemmer = Stemmer("english")
	summarizer = TextRankSummarizer(stemmer)
	summarizer.stop_words = get_stop_words("english")
	summary = summarize(doc, summarizer)
	return summary

def luhnn(doc):
	stemmer = Stemmer("english")
	summarizer = LuhnSummarizer(stemmer)
	summarizer.stop_words = get_stop_words("english")
	summary = summarize(doc, summarizer)
	return summary

def klsumm(doc):
	stemmer = Stemmer("english")
	summarizer = KLSummarizer(stemmer)
	summarizer.stop_words = get_stop_words("english")
	summary = summarize(doc, summarizer)
	return summary


def lsaa(doc, debug = False):
	stemmer = Stemmer("english")
	summarizer = LsaSummarizer(stemmer)
	summarizer.stop_words = get_stop_words("english")
	summary = summarize(doc, summarizer)
	return summary

if __name__ == '__main__':
	
	file = "ent5.txt"
	parser = PlaintextParser.from_file(file, Tokenizer("english"))

	rfile = "ent5sum.txt"
	refparser = PlaintextParser.from_file(rfile, Tokenizer("english"))
	refparser = refparser.document.sentences

	print(lsa(parser,refparser,True))
