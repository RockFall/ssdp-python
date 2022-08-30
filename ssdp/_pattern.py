class Pattern:
  # Static vars
  numeroIndividuosGerados = 0
  vrPCount = []
  vrNCount = []

  def __init__(self, items, fitnessFunc):
    self.items = items
    self.fitnessFunc = fitnessFunc
    self.vrP = []
    self.vrN = []
    self.TP = 0 # positive support = |c+(dp)|
    self.FP = 0 # negative support = |c-(dp)|
    self.quality = 0.0
    self.synonyms = []
    self.subPatterns = []
