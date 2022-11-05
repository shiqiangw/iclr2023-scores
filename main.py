import openreview
import numpy as np

client = openreview.Client(baseurl='https://api.openreview.net')

submissions = client.get_all_notes(invitation="ICLR.cc/2023/Conference/-/Blind_Submission", details='directReplies')

reviews = []
for submission in submissions:
    reviews = reviews + [reply for reply in submission.details["directReplies"] if reply["invitation"].endswith("Official_Review")]

scores_dict = {}
for r in reviews:
    if r['forum'] not in scores_dict:
        scores_dict[r['forum']] = []
    scores_dict[r['forum']].append(int(r['content']['recommendation'].split(':')[0]))

with open('output.csv', 'w') as f:
    f.write('Title,Average Score,Standard Deviation,Individual Scores,Author-defined Area\n')

    statistics = []
    for s in submissions:
        if s.forum not in scores_dict:
            continue
        title = s.content['title']
        if 'Please_choose_the_closest_area_that_your_submission_falls_into' in s.content:
            area = s.content['Please_choose_the_closest_area_that_your_submission_falls_into']
        else:
            area = ''
        scores = scores_dict[s.forum]
        avg_score = np.mean(scores)
        std_score = np.std(scores)
        f.write('\"' + title + '\",' + str(avg_score) + ',' + str(std_score) + ',' + ';'.join([str(i) for i in scores]) + ',\"' + area + '\"\n')

