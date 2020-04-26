import abc

'''
Intended C++ template:
    activate()
        Launch and init the engine
    deactivate()
        Stop engine process
    isActive()
    
    startAnalysis(time/steps)
    
    stopAnalysis()
    
    isAnalyzing()
    
    setTimeLimit()
    
    error()
    
    getAnalysis()
    
    updateLog()
    
    
    

'''



class Stockfish:
    def midgameScore(self):
        pass

    def endgameScore(self):
        pass

class Score(abc.ABC):
    def score(self):
        pass

    def toMate(self):
        pass

    def midGameEvaluation(self):
        pass
