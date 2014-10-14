;; returns true for perfect numbers, false otherwise
;; perfect number = sum of its divisors except the number itself
(defn perf-num
   [n]
   (if 
     (= (reduce + (into [] (filter (comp zero? (partial rem n)) (range 1 n)))) n)
     true
     false)
)
