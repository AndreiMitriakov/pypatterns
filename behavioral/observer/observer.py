#!/usr/bin/env python3
# coding: utf-8

class JobPost:

    def __init__(self, title):
        self.title = title

    def get_title(self):
        return self.title

class JobSeeker:
    
    def __init__(self, name):
        self.name = name

    def on_job_posted(self, job):
        print('Hi, {}, new job is posted: {}'.format(self.name, job.get_title()))

class JobPostings:
    
    def __init__(self):
        self.observers = []

    def notify(self, job_post):
        for observer in self.observers:
            observer.on_job_posted(job_post)

    def attach(self, observer):
        self.observers.append(observer)

    def add_job(self, job_post):
        self.notify(job_post)


if __name__ == '__main__':
    john_doe = JobSeeker('John Doe')
    jane_doe = JobSeeker('Jane Doe')

    job_postings = JobPostings()
    job_postings.attach(john_doe)
    job_postings.attach(jane_doe)

    job_postings.add_job(JobPost('Software Engineer'));
