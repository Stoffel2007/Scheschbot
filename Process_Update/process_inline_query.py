import inline_results


def get_message_list(inline_query):
    params_dict = {'inline_query_id': inline_query.id,
                   'results': inline_results.get_inline_results(inline_query.query)}
    return [{'action': 'inline', 'params_dict': params_dict}]
