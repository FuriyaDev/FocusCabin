def user_profile_image_directory_path(instance, filename):
    return f"users/{instance.id}/profile_image/{filename}"


def passport_upload_path(instance, filename):
    return f"users/{instance.id}/passport/{filename}"
