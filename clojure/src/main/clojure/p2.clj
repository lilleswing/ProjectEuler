(defn fib-seq []
  ((fn rfib [a b]
     (cons a (lazy-seq (rfib b (+ a b)))))
    0 1))

(defn solve []
  (->> (fib-seq)
    (take-while #(< %1 4000000))
    (filter even?)
    (reduce +)))

(println (solve))
