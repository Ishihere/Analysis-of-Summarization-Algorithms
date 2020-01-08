from sumy.evaluation import cosine_similarity
from sumy.evaluation import unit_overlap
from sumy.evaluation import precision
from sumy.evaluation import recall
from sumy.evaluation import f_score
from sumy.models import TfDocumentModel
from sumy.nlp.tokenizers import Tokenizer

def sumtostr(summary):
	sumstr = ""
	for line in summary:
		sumstr += " " + str(line)
	return sumstr

def sumtotup(summary):
	sumtup = tuple()
	for line in summary:
		sumtup = sumtup + (str(line),)
	return sumtup

def evaluate(summary, sumref, debug=False):
	sumstring = sumtostr(summary)
	sumtuple = sumtotup(summary)
	refstring = sumtostr(sumref)
	reftuple = sumtotup(sumref)
	summodel = TfDocumentModel(sumstring, Tokenizer("english"))
	refmodel = TfDocumentModel(refstring, Tokenizer("english"))

	if debug:
		print(reftuple)
		print(sumtuple)

	cos_val = cosine_similarity(summodel, refmodel)
	unit_val = unit_overlap(summodel, refmodel)

	precision_val = precision(sumtuple, reftuple)
	recall_val = recall(sumtuple, reftuple)
	f_val = f_score(sumtuple, reftuple)

	return cos_val, unit_val, precision_val, recall_val, f_val
