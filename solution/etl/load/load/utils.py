from load.constants import USER_SESSION_STATS_JOB_TABLE_NAME, MATCH_STATS_JOB_TABLE_NAME


def get_table_name_by_job(job: str) -> str:
    if job == "user-session-stats":
        return USER_SESSION_STATS_JOB_TABLE_NAME
    else:
        return MATCH_STATS_JOB_TABLE_NAME