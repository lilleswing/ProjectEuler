(ns
  ^{:author leswing}
  euler.p3)

(defn prime-factors [n]
  (loop [n n divisor 2 factors []]
    (if (< n 2)
      factors
      (if (= 0 (rem n divisor))
        (recur (/ n divisor) divisor (conj factors divisor))
        (recur n (inc divisor) factors)
        )
      )
    )
  )

(defn solve [x]
  (apply max (prime-factors x))
  )

(println (solve 600851475143))
