playMonty <- function () {
 
        wins = 0
        door = 1:3
        strategy <- NA
        numTrials <- NA
        
        print("Welcome to Monty Hall simulation")
        print("***")
        print("Choose your play strategy")
        
        while(is.na(strategy)== TRUE){
        ans <- readline("0 for switch, 1 for stay, 2 for random: ")
        if(ans=="0"){strategy <- "switch"}
        if(ans=="1"){strategy <- "stay"}
        if(ans=="2"){strategy <- "random"}  
        }
        while(is.na(numTrials) == TRUE){
        ans <- readline("How many games should we simulate?: ")
        numTrials <- as.integer(ans)
        }
        
        for(trial in 1:numTrials){
              prize <- sample(door,1)
              guess <- sample(door,1)
              
              if (guess != prize)
                    reveal <- door[-c(guess,prize)]
                    
              else
                    reveal <- sample(door[-(prize)],1)
              
              
            if (strategy=="stay"){select <- guess}
            if (strategy =="switch"){select <- door[-c(reveal,guess)]}
            if (strategy =="random"){select <- sample(door[-c(reveal)],1)}
            
            if(prize == select){wins <- wins + 1}
        }
            
        result <- (wins / numTrials * 100)
        
        print(paste("When playing ", numTrials, " games, with the ",strategy, " strategy, "," wins occured in ", round(result,3), "% cases. " ))
        
        }
