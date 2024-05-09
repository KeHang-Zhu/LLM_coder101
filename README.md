# An Overview of LLM coder 101 | Kehang & Haonan


---

## Motivation:

I was a physicist until 2 years ago. Writing codes was a daunting job back then, especially in the region of computational physics. The old code base is written in Fortran and Matlab. One needs to search in the old documents for decades to find a simple line of explanation of a function. No example was provided. And one needs some real genius to make it work.

This is all gone in the LLM era when one just needs to ask LLM to write the code. But this is not penicillin. One still needs some basic knowledge in Computer Science to master the techniques of coding. And I am sad to find that, today, major colleges are still teaching coding in the same way as the pre-GPT era. A student still needs to learn how to search the documentation and find the right usage of a function or object.

So, I am starting this blog to share my thoughts on how to learn coding in this new era (partly as my personal experience in learning coding as well).

### To dive in, the mindsets below will be important:

- Fast feedback loop. Don’t be afraid of errors. As a beginner, errors will help you learn.
- Get the code to work first! As a beginner, forget about the simplicity or efficiency for now.

We will use an example --Build a boyfriend/girlfriend chatbot -- to start our journey with LLM coder. We hope it will be fun.

### Here is the outline of the journey:

- Overview of the goals and the basic components required.
- Environment:
    - How to install necessary software and set up your development workspace.
- Frontend
- Backend
    - OpenAI API
    - open-sourced model
- Algorithms
    - Fine-tuning
- Database
    - Server memory
    - SQLite
    - Cloud
- development
    - local development
    - migrate to Google Cloud
