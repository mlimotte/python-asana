# This file is automatically generated by generate.py using api.json

class _Attachments:
    def __init__(self, client=None):
        self.client = client

    def find_by_task(self, task_id, params={}, **options):
        """Dispatches a GET request to /tasks/:taskId/attachments of the API to get all attachments associated with the task."""
        path = '/tasks/%d/attachments' % (task_id)
        return self.client.get_collection(path, params, **options)

    def find_by_id(self, attachment_id, params={}, **options):
        """Dispatches a GET request to /attachments/:attachmentId of the API to get information about the attachment."""
        path = '/attachments/%d' % (attachment_id)
        return self.client.get(path, params, **options)
