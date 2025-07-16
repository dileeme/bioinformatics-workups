def dominant_phenotype_probability(k, m, n):
    total = k + m + n
    total_pairs = total * (total - 1) / 2
    
    dom = 1.0 * (k * (k - 1)) / 2       
    dom += 1.0 * k * m                 
    dom += 1.0 * k * n                  
    dom += 0.75 * (m * (m - 1)) / 2     
    dom += 0.5 * m * n                  
  

    return dom / total_pairs
    print(dominant_phenotype_probability(2, 2, 2))  
