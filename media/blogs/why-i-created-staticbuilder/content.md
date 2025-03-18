As developers, we often find ourselves juggling between multiple tasks, from writing code to maintaining websites, and even creating and maintaining personal portfolios or blogs. One of the key aspects of managing a portfolio or blog is ensuring that it looks sleek, and that it does not cost an unreasonable amount of money to maintain. That's exactly why I created [**StaticBuilder**](https://github.com/IliyaBadri/StaticBuilder)—a Python-powered tool designed to generate static websites for my GitHub Pages webpage. After all, who doesn't love a free personal webpage and blog? (Thanks to GitHub's generous features)

### What is StaticBuilder?

**StaticBuilder** is a small project I created to streamline the process of turning a collection of JSON and Markdown files into a fully functional static webpage. This tool helped me save time and effort by automatically generating a webpage that’s ready to go live on GitHub Pages.

Setting it up is simple: just modify the JSON and Markdown files, run the Python script, and you're good to go! And because it’s main target is building fully static pages that are deployable to **GitHub Pages**, it’s a fantastic option for those looking to deploy a free static website quickly and reliably.

Also, I made the project really modular. This makes it easy for anyone to build their own webpage. For example, if you want to change the text on a specific button, you just modify the corresponding JSON file. Or if you don't like the theme of the webpage, you can open the python file related to it and change the hard-coded HTML template in it. Styling is handled by Tailwind CSS, a utility-first framework that makes it easy to design responsive websites quickly. In general, there are no fancy thing's going on with it. It's all low-level and simple. Unlike the trendy libraries and frameworks that are popular today.

### The Challenge of Static Websites

The web has come a long way, and today’s websites are dynamic, interactive, and packed with features. However, static websites continue to hold significant value, especially for personal blogs, portfolios, and documentation sites. Static websites are simple to deploy, fast to load, and cheap to serve. They're also often easier to maintain compared to dynamic websites, which require constant backend updates.

Despite these benefits, creating a good-looking static website can be a tedious process. It requires manual HTML, CSS, and sometimes JavaScript. What if we could automate this? This is exactly why I created **StaticBuilder**: to automate the tedious process of building a static site.

### More Details

StaticBuilder simplifies the entire process, transforming a folder of JSON and Markdown files into a fully functional static site.

Once you've structured your JSON and Markdown files to contain your content and configurations... all you need to do is run a simple Python script—`main.py`—and voilà! StaticBuilder processes all the data and outputs a sleek, styled static site in your `static` directory. It even starts a test server, so you can preview your site locally before pushing it live to GitHub Pages. That's some great automation, isn't it?

### A Word on Open Source and Collaboration

StaticBuilder is an open-source project that's available on [GitHub](https://github.com/IliyaBadri/StaticBuilder), meaning anyone can contribute to its growth and improvement. Although it's a personal project but if you find any bugs or have ideas for new features, I encourage you to open issues or submit pull requests. I really appreciate that.

### Conclusion

I personally think building a website shouldn’t be a hassle. I personally believe automating repetitive tasks like this is a game changer, saving time and effort that can be spent elsewhere. And I also believe that extra frameworks are not needed and will only bloat the workflow and final result. 

With **StaticBuilder** I could easily automate the process of creating a static site, Which is just raw HTML, CSS and JavaScript. Also there are no fancy API's; It's just JSON, Markdown, and hard-coded HTML templates inside python files.  leaving me more time to focus on what really matters—your content.

Feel free to check out the project on [GitHub](https://github.com/IliyaBadri/StaticBuilder).
