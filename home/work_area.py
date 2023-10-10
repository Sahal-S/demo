
    if request.method=='POST':
        print("method post......")
        role=request.POST['role']
        print(role)
        user_name=request.POST['username']
        print(user_name)
        pass_word=request.POST['password']
        print(pass_word)
        re=request.POST['re']
        print(re)
        com_pany=request.POST['company']
        print(com_pany)
        
        #authentification for company
        if role=='company':   

            if pass_word==re:
                d=User.objects.create_user(username=user_name,password=pass_word)
                d.save()
                return redirect('home')
            else:
                ls=User.objects.all()
                return render(request,'signup.html',{'ls':ls})
        
        #authentification for employe    
        else:   
            if pass_word==re:
                d=employe(username=user_name,password=pass_word,company=com_pany)
                d.save()
                return redirect('home')
            else:
                ls=User.objects.all()
                return render(request,'signup.html',{'ls':ls})
        

        
    else:   
        print("else condition................")
        ls=User.objects.all()
        return render(request,'signup.html',{'ls':ls})