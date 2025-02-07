"""
//******************************************************************************
// FILENAME:           cog_test_score_extractor.py
// DESCRIPTION:        This Natural Language Processing Python script contains pseudocode for extracting MoCA and MMSE
//                     test scores from clinical note text.
// AUTHOR(s):          John Novoa-Laurentiev
//
// For those interested in learning more about this model, contact us at BWHMTERMS@bwh.harvard.edu .
//******************************************************************************
"""


def find_scores_in_sents(input_file, output_file):
    # high priority regex try to capture scores with the maximum present in text, e.g. "24/30" rather than just "24"
    high_priority_regex_patterns = [
        compile(rf'regex pattern 1'),
        compile(rf'regex pattern 2'),
    ]
    low_priority_regex_patterns = [
        compile(rf'regex pattern 1'),
        compile(rf'regex pattern 2'),
    ]
    regex_patterns = [
        compile(rf'regex pattern 1'),
        compile(rf'regex pattern 2'),
    ]

    # process note data
    found_scores = []
    with open(input_file, 'r', encoding='utf-8') as f:
        for line in f:
            if line:
                score_matches = []
                sent_data = line.split('\t')
                sent_id = '_'.join(sent_data[:-1])
                sent_text = sent_data[-1].strip().lower()
                for pattern in high_priority_regex_patterns:
                    score_matches.extend(pattern.findall(sent_text))
                high_priority_match_tests = [test for test, score in score_matches]  # test results found so far
                for pattern in low_priority_regex_patterns:
                    low_priority_matches = pattern.findall(sent_text)
                    for test, score in low_priority_matches:
                        # if match was previously found for the same test, ignore it
                        if test not in high_priority_match_tests:
                            score_matches.append((test, score))
                for pattern in regex_patterns:
                    score_matches.extend(pattern.findall(sent_text))
                found_scores.append((sent_id, sent_text, score_matches))

    # write to .csv
    with open(output_file, 'w', encoding='utf-8', newline='') as f:
        match_result_writer = writer(f)
        match_result_writer.writerow(['id', 'text', 'test_match', 'score_match'])
        for idx, sent_text, sent_matches in found_scores:
            if sent_matches:
                # write all test score matches
                for test_match, score_match in sent_matches:
                    # skip cases where a score match exceeds the maximum possible score
                    if int(score_match) > test_maxima_map[test]:
                        continue
                    match_result_writer.writerow([idx, sent_text, test_match, score_match])
            else:
                # if no matches write sentence data with no matches
                match_result_writer.writerow([idx, sent_text, 'NONE', 'NONE'])


if __name__ == '__main__':
    for note_type in note_type_list:
        input_file = ''
        output_file = ''
        find_scores_in_sents(input_file, output_file)
