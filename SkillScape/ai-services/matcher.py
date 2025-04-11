def match_user_to_gig(user_skills, gigs_db):
    matched = []
    for gig in gigs_db:
        if any(skill in gig['required_skills'] for skill in user_skills):
            matched.append(gig)
    return matched