def solution(max_weight, specs, names):
    answer = 1
    specs_dict = dict(specs)
    products_weight = 0

    for name in names:
        now_product_weight = int(specs_dict[name])
        products_weight += now_product_weight

        if products_weight > max_weight:
            answer += 1
            products_weight = now_product_weight
        elif products_weight == max_weight:
            answer += 1
            products_weight = 0

    return answer