#!/usr/bin/env python3

import classify

def update_readme():
    """Update README.md with visualizations for data sets."""
    with open('README.md') as f:
        text = f.read()
        begin_mark = '<!-- BEGIN AUTO -->\n'
        end_mark = '<!-- END AUTO -->\n'
        header = text[:text.index(begin_mark) + len(begin_mark)]
        footer = text[text.index(end_mark):]

    lines = []

    lines.append('Training Images\n')
    lines.append('---------------\n')
    lines.append('<table>\n')
    for i, (fname, out) in enumerate(classify.classify_images('train-set')):
        if i == 0 or i % 5 == 0:
            lines.append('<tr>\n')
        lines.append('  <td>\n\n ![Training Image {}]({})\n'.format(i, fname))
    lines.append('</table>\n\n\n')

    lines.append('Test Results\n')
    lines.append('------------\n')
    corrects = 0
    total = 0
    lines.append('<table>\n')
    for i, (fname, out) in enumerate(classify.classify_images('test-set')):
        if i == 0 or i % 5 == 0:
            lines.append('<tr>\n')

        correct = (out == 'cat' and 'cat' in fname or
                   out == 'not' and 'cat' not in fname)
        comment = '(pass)' if correct else '(fail)'

        lines.append('  <td>\n\n  ![Test Image {}]({})<br>\n'.format(i, fname))
        lines.append('  <span>{} {}</span>\n'.format(out, comment))

        if correct:
            corrects += 1
        total += 1
    lines.append('</table>\n\n\n')

    lines.append('Test Accuracy\n')
    lines.append('-------------\n')
    lines.append('Out of {} test samples, {} were correctly classified.\n\n'
                 .format(total, corrects))
    lines.append('The test accuracy is: {:.2f}%.\n'
                 .format(100 * corrects / total))

    output = header + ''.join(lines) + footer
    with open('README.md', 'w') as f:
        f.write(output)


if __name__ == '__main__':
    update_readme()
