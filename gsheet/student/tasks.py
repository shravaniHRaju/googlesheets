from celery import shared_task
from time import sleep


@shared_task
def process_student_data(student_id):
    # Process student data asynchronously
    sleep(5)  # Simulate long-running task
    return f"Processed data for student with id {student_id}"