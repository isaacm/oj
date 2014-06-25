;; clojure problem 'To Tree, or not to Tree'
(fn is-btree? [[rt lc rc :as x]]
  (cond
    (some false? x) false
      (= 3 (count x)) (and (if (coll? lc) (is-btree? lc) true)
                      (if (coll? rc) (is-btree? rc) true)
                      (not (or (nil? rt) (coll? rt))))
      :else false))
