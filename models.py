class BlogRepository:
    pass    

    def GetBlog(self, blogId):
        exampleBlog1 = Blog()
        exampleBlog1.title = 'Example Blog #1'
        exampleBlog1.text = 'This is the example blog #1 text.'
        exampleBlog1.description = ''
        exampleBlog1.id = 10

        exampleBlog2 = Blog()
        exampleBlog2.title = 'Totally Different #2'
        exampleBlog2.text = 'The quick brown blog#2 fox jumped <i>over</i> the lazy log.'
        exampleBlog2.description = ''
        exampleBlog2.id = 11

        if blogId == 1:
            return exampleBlog1
        if blogId == 2:
            return exampleBlog2        

class Blog:
    pass