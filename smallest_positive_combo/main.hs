import System.Environment
import Data.List

powerDifference a b = (33^a) - (7^b)
minValue max = minimum
                $ take max
                $ zipWith powerDifference [1..] [1..]




