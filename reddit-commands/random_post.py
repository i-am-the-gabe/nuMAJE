@bot.command()
async def random_post(ctx, args):

    async with ctx.channel.typing():                                        
        rp_result = discord.Embed(title= "Random Reddit Post", colour=red)
        sub = reddit.subreddit(args)                                        
        if not sub.over18:

            post = list(sub.hot(limit=60))                                  
            re = random.choice(post)                                       

            while re.over_18:
                re = random.choice(post)                                    

            rp_result.title = re.title                                      
            rp_result.url = re.url                                          
            rp_result.set_footer(text="\nPosted by u/" + str(re.author))   

            if not re.is_self:                                              
                rp_result.set_image(url=re.url)                             

            else:
                rp_result.description = re.selftext                         
        else:
            #sub over 18
            rp_result.title="Sorry, I can't share that!"
            rp_result.description="That's an NSFW subreddit."

    await ctx.send(embed=rp_result)
