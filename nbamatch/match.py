'''Apply SVM to rank the similarity between a new player and NBA pro players'''
'''Author: Dayang Xiang'''
import numpy as np
import scipy.spatial.distance as spd
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC

def proj3(pos, x): # pos: position, x: new data point
      if pos == 'C': # XTrain: training data for NB, yTrain: training labels for NB
            XTrain = np.loadtxt('Ctrain.txt')
            #yTrain = np.loadtxt('CtrainL.txt')
            XTest = np.loadtxt('C.txt')
            yTest = np.loadtxt('Clabs.txt')
      elif pos == 'PF':
            XTrain = np.loadtxt('PFtrain.txt')
            #yTrain = np.loadtxt('PFtrainL.txt')
            XTest = np.loadtxt('PF.txt')
            yTest = np.loadtxt('PFlabs.txt')
      elif pos == 'PG':
            XTrain = np.loadtxt('PGTrain.txt')
            #yTrain = np.loadtxt('PGtrainL.txt')
            XTest = np.loadtxt('PG.txt')
            yTest = np.loadtxt('PGlabs.txt')
      elif pos == 'SF':
            XTrain = np.loadtxt('SFTrain.txt')
            #yTrain = np.loadtxt('SFtrainL.txt')
            XTest = np.loadtxt('SF.txt')
            yTest = np.loadtxt('SFlabs.txt')
      elif pos == 'SG':
            XTrain = np.loadtxt('SGTrain.txt')
            #yTrain = np.loadtxt('SGtrainL.txt')
            XTest = np.loadtxt('SG.txt')
            yTest = np.loadtxt('SGlabs.txt')
      else:
            print "Please reinput the position."

      D = XTrain.shape[1] # number of features
      #NBtr = GaussianNB()
      #NBtr.fit(XTrain, yTrain)
      #ytr = NBtr.predict(x) # predicting the class of x (w.r.t training data)
      NBte = GaussianNB()
      NBte.fit(XTest, yTest)
      yTrain = NBte.predict(XTrain) # predicting the classes of XTrain's rows
      yte = NBte.predict(x) # predicting the class of x (w.r.t testing data)

      '''create training data from the players (2009-2011) in the same class as x (ytr)'''
      tmpTrain = np.zeros(D) # create training data for Ranking SVM
      TrIndex = [] # store the indices of tmpTrain
      for i in range(len(yTrain)):
            if yTrain[i] == yte: # the same class as new data point                 
                  tmpTrain = np.vstack((tmpTrain, XTrain[i]))
                  TrIndex = np.append(TrIndex, i)
            else: # different classes from new data point
                  pass
      tmpTrain = np.delete(tmpTrain, 0, 0) # delete the initializing row

      '''calculate correlation distances between rows of tmpTrain and x'''
      TrCorrD = np.zeros(np.shape(TrIndex)) # initialize correlation distances
      for i in range(len(TrCorrD)):
            TrCorrD[i] = spd.correlation(tmpTrain[i], x)
      TrRank = np.argsort(TrCorrD)
      if len(TrIndex) < 10:
            noTrPts = len(TrIndex)
      else:
            noTrPts = 10 # select top 10 relevant training points
      vecTrain = tmpTrain[TrRank[:noTrPts]]
      #print TrIndex[TrRank[:noTrPts]]

      '''create training feature vectors'''
      noFt = 2 # number of features
      ftTrain = np.zeros((noTrPts,noFt))
      for i in range(noTrPts):
            ftTrain[i] = np.array([spd.euclidean(vecTrain[i],x), spd.cosine(vecTrain[i],x)])

      '''create taining matrix and labels for SVM from vecTrain and TrRank'''
      SVMTrain = np.zeros((noTrPts*(noTrPts-1), noFt))
      SVMLabel = np.zeros(np.shape(SVMTrain)[0]) - 1
      for i in range(noTrPts):
            for j in range(noTrPts):
                  if i > j:
                        SVMTrain[i*(noTrPts-1)+j] = ftTrain[i] - ftTrain[j]
                        if TrRank[i] < TrRank[j]: # smaller rank => closer distance
                              SVMLabel[i*(noTrPts-1)+j] = 1
                        else:
                              SVMLabel[i*(noTrPts-1)+j] = 0
                  elif i < j:
                        SVMTrain[i*(noTrPts-1)+j-1] = ftTrain[i] - ftTrain[j]
                        if TrRank[i] < TrRank[j]:
                              SVMLabel[i*(noTrPts-1)+j-1] = 1
                        else:
                              SVMLabel[i*(noTrPts-1)+j-1] = 0
                  else:
                        pass #if i == j, pass


      '''create testing data from the players (2011-2015) in the same class as x (ytr)'''
      tmpTest = np.zeros(D) # extract data of the same class of x in testing data
      TeIndex = [] # store the indices of testing data
      for i in range(len(yTest)):
            if yTest[i] == yte: # the same class as new data point
                  tmpTest = np.vstack((tmpTest, XTest[i]))
                  TeIndex = np.append(TeIndex, i)
            else:
                  pass
      tmpTest = np.delete(tmpTest, 0, 0) # delete the initializing row
      
      '''calculate correlation distances between testing data and x'''
      TeCorrD = np.zeros(np.shape(TeIndex))
      for i in range(len(TeCorrD)):
            TeCorrD[i] = spd.correlation(tmpTest[i], x)
      TeRank = np.argsort(TeCorrD)
      noTePts = noTrPts # select top 10 relevant testing points
      vecTest = tmpTest[TeRank[:noTePts]]
      #print TeIndex[TeRank[:10]]
      '''calculate NDCG'''
      TeGrade = np.arange(noTePts,0,-1)
      TeGains = 2 ** TeGrade - 1
      TeDisct = 1 / np.log2(np.arange(2,2+noTePts))
      TeDcg = np.zeros((noTePts))
      for i in range(noTePts):
            TeDcg[i] = TeDcg[i-1] + TeGains[i]*TeDisct[i]

      '''create testing feature vectors'''
      ftTest = np.zeros((noTePts,noFt))
      for i in range(noTePts):
            ftTest[i] = np.array([spd.euclidean(vecTest[i],x), spd.cosine(vecTest[i],x)])

      '''create testing matrix and labels for SVM from vecTest and TeRank'''
      SVMTest = np.zeros((noTePts*(noTePts-1), noFt))
      TeLabs = np.zeros(np.shape(SVMTest)[0]) - 1 # testing labels (used as a comparion with results)
      for i in range(noTePts):
            for j in range(noTePts):
                  if i > j:
                        SVMTest[i*(noTePts-1)+j] = ftTest[i] - ftTest[j]
                        if TeRank[i] < TeRank[j]:
                              TeLabs[i*(noTePts-1)+j] = 1
                        else:
                              TeLabs[i*(noTePts-1)+j] = 0
                  elif i < j:
                        SVMTest[i*(noTePts-1)+j-1] = ftTest[i] - ftTest[j]
                        if TeRank[i] < TeRank[j]:
                              TeLabs[i*(noTePts-1)+j-1] = 1
                        else:
                              TeLabs[i*(noTePts-1)+j-1] = 0
                  else:
                        pass

      '''train the ranking SVM'''
      clf = SVC(C=0.01, kernel='linear')
      clf.fit(SVMTrain, SVMLabel)
      pred_labels = clf.predict(SVMTest) # predict labels
      visTest = np.reshape(pred_labels, (noTePts,noTePts-1)) # make the testing results visualized
      ids = (-np.sum(visTest, axis=1)).argsort()[:noTePts] # descending order
      ReIndex = TeIndex[TeRank[:noTePts]][ids] # ranking svm results of testing data (indices)
      return ReIndex
      '''calculate NDCG'''
      ReGrade = np.zeros((noTePts))
      for i in range(noTePts):
            for j in range(noTePts):
                  if ReIndex[i] == TeIndex[TeRank[:noTePts]][j]:
                        ReGrade[i] = TeGrade[j]
                  else:
                        pass
      ReGains = 2 ** ReGrade - 1
      ReDisct = TeDisct
      ReDcg = np.zeros((noTePts))
      for i in range(noTePts):
            ReDcg[i] = ReDcg[i-1] + ReGains[i]*ReDisct[i]
      ReNdcg = ReDcg / TeDcg
      #return ReNdcg[noTePts-1]

#proj3('C', [0.34,0.84,0.63,0.28,0.87,1])
#proj3('PF', [0.12,0.5,0.,0.02,0.05,0.1])
#proj3('PG', [0.71,0.73,0.35,0.55,0.5,0.63,0.37])
#proj3('SF', [0.87,0.43,0.32,0.68,0.72,0.75,0.76,0.36])
#proj3('SG', [0.41,0.51,0.39,0.78,0.35,0.72,0.67])
'''summ = 0
for i in range(1):
      summ += proj3('SG', np.random.rand(1,6))
print summ/1'''
