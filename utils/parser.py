def prepare_resume_jd_prompt(
        resume_text,
        jd_text
):

    return f"""
RESUME

{resume_text}

-----------------------------------

JOB DESCRIPTION

{jd_text}
"""