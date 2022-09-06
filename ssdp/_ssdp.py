from ._pattern import Pattern
import pandas as pd

class SSDP:
  """
  _parameter_constraints: dict = {
    "fitnessFunc": [
      "QG", "SUB", "WRACC"
    ]
  }
  """

  def __init__(
    self,
    df=None,
    path="",
    target="p",
    k=10,
    fitnessFunc="QR",
    discretizationType="None"
  ):
    self.df = df
    self.path = path
    self.target = target
    self.k = k
    self.fitnessFunc = fitnessFunc
    self.discretizationType = discretizationType

  def _validate_params(self):
    error = "None"
    if self.fitnessFunc not in ["QG", "SUB", "WRACC"]:
      error = "Invalid parameter"
    if self.target not in ["p", "n", "positive", "negative"]:
      error = "Invalid parameter"

  def _get_path_data(self, path):
    if

  def run(self, df=None, path="", k=None, fitnessFunc=None) -> "list[Pattern]":
    self._validate_params()

    if df == None:
      if path == "":
        raise ValueError("You must enter either a file Path or a pandas DataFrame as a parameter")
      df = pd.read_csv(path)
      self._get_path_data(path)

    #self._check_discretization(X)

    p = Pattern(k, fitnessFunc)
    return [p for n in range(k)]
