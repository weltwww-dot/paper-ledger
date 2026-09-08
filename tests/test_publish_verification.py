import sys
import unittest
from pathlib import Path


SCRIPTS = Path(__file__).resolve().parents[1] / "scripts"
sys.path.insert(0, str(SCRIPTS))

from run_update import PublishVerificationError, verify_pages_release  # noqa: E402


class PublishVerificationTests(unittest.TestCase):
    def test_accepts_built_pages_for_current_commit_with_matching_content(self):
        result = verify_pages_release(
            build_status="built",
            build_commit="abc123456789",
            head_sha="abc123456789",
            local_fingerprint="same",
            remote_fingerprint="same",
        )

        self.assertTrue(result)

    def test_rejects_matching_count_content_until_pages_is_built(self):
        with self.assertRaisesRegex(PublishVerificationError, "Pages 构建"):
            verify_pages_release(
                build_status="building",
                build_commit="abc123456789",
                head_sha="abc123456789",
                local_fingerprint="same",
                remote_fingerprint="same",
            )

    def test_rejects_pages_built_for_another_commit(self):
        with self.assertRaisesRegex(PublishVerificationError, "当前提交"):
            verify_pages_release(
                build_status="built",
                build_commit="old-commit",
                head_sha="abc123456789",
                local_fingerprint="same",
                remote_fingerprint="same",
            )

    def test_rejects_stale_online_content_after_pages_build(self):
        with self.assertRaisesRegex(PublishVerificationError, "线上内容"):
            verify_pages_release(
                build_status="built",
                build_commit="abc123456789",
                head_sha="abc123456789",
                local_fingerprint="local",
                remote_fingerprint="stale",
            )


if __name__ == "__main__":
    unittest.main()
