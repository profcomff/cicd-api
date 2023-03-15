import argparse
import re
from subprocess import Popen


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--repo-url', type=str, required=True)
    parser.add_argument('--git-ref', type=str, required=True)
    return parser.parse_args()


if __name__ == "__main__":
    args = get_args()
    org, repo = args.repo_url.removeprefix('https://github.com/').rsplit('/', 1)
    pr_num = re.match("^refs/pull/(?P<pr_num>\d+)", args.git_ref).group('pr_num')
    Popen(['docker', 'rm', '-f', f'pkff_dev__{repo}__pr-{pr_num}']).communicate()
