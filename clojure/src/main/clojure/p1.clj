(defn isbuzz [x]
  (or (zero? (mod x 3)) (zero? (mod x 5)))
  )

(defn solve [x]
  (->> (range x)
    (filter isbuzz)
    (reduce +))
  )

(println (solve 1000))
