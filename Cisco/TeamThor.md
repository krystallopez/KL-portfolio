# Team THOR 

Team THOR, is a Cisco engineering team that builds and maintains internal tooling in Cisco Umbrella, a cloud-security platform that provides an additional line of defense against malicious software and threats on the internet by using threat intelligence.  

Team THOR works with other teams as well to help maintain CHIM and all of its dependencies.


## CHIM (Change & Incident Management)

CHIM (Change & Incident Management) is a project created to build and improve tooling to help teams within Cisco Umbrella with the Incident Management and Change Management Procedures. The goal of CHIM is to facilitate automation around Change and Incident managment in order to help standardize the way teams implement change and incident management procedures by offering a set of tools that are easy to use and simple to integrate into any team's current workflow. 

In CHIM, users can report outages that can occur within the microservices that build Cisco Umbrella. CHIM is used to record outages, incidents, change notices, and deployments. CHIM is also available to users should they want to build off the CHIM API they can do so. There are two APIs that are available in CHIM, the <code>UserApi</code> and the <code>DeploymentApi</code>. 

With the <code>UserApi</code>, a user can leverage the CHIM API for automation tasks, such as intergrating change notice created into build pipelines. Users can gain access to the API using API Tokens with permissions, each API token is associated with the user who requested it. A user can create an API key directly within in CHIM. With the <code>DeploymentApi</code>, a user can create a deployment access key in order to create a new software deployment. This API will allow users to trigger validation of change tickets and create Deploy Artifacts. The <code>DeploymentApi</code> also allows stakeholders to keep track of all deployments that take place in CHIM for each microservice that makes up Cisco Umbrella. 

In CHIM, a user can also post their Retrospectives. Retrospectives are documents that include details of an incident/outage, who created the outage, how the outage was resolved, and what things can be done differently to ensure a similar outage does not happen. Each retropsective will also include an incident overview, a detailed timeline, root causes, the services and customers that were impacted, as well as metrics assocaited with the outage. CHIM records all of this in a more readable manner so that is easily accessible to stakeholders. 

CHIM Users can also create "Mock" incidents and outage in a very cool feature that was created called FireDrill mode. In FireDrill mode, a user can create a "mock" incident without alerting any official channels. Any incidents that are created in Firedrill mode do not create ant real or active incidents, but instead will mock real instances of outages and store in the database. 

Overall, CHIM is a vital tool that helps support Cisco Umbrella's internal and external customers daily by providing an automated approach to change and incident management. 


## SDT (Software Deployment Tracker)

In April 2023, myself and my team were tasked with building another aspect of CHIM, this was project was called SDT, also known as, Software Deployment Tracker. This was one of the first major projects that I was part of. The Software Deployment Tracker is a service that enables the deployment pipelines to validate that a change ticket has been approved prior to deployment. The SDT also provides a REST API that can be integrated with other systems and tools in the deployment pipeline. It also captures and stores data related to deployments and rollbacks. 

My contributions to this project are as follows:

- I collaborated with my team in the creation of the SDT UI in CHIM that would allow a user to submit a manual deployment. This included creating a form that would allow the user to enter in all deployment information, such as the target environment, the build job URL, the service that is creating the deployment, as well as the deployment status. 

- The means to create a manual deployment was placed into a modal on that UI so that the user can easily create a manual deployment. Using <code>Formik</code> and <code>Yup</code> I was able to set up the inital values for the form and determine what information would be required in order to successfully submit a manual deployment through the CHIM UI. 

- I collaborated with my mentors to create all of the UI endpoints for the <code>DeploymentClient</code> class, as well the deployment query keys needed, which allow a user to look up specific deployments based on keywords entered in a search bar on the Deployment Dashboard page.

-  Established an export function so that all details of a deployment can be exported into a CSV file. 

- In order for users to be able to created deployments using the <code>DeploymentApi</code>, deployment access keys needed to be implemented. For SDT, I created a deployment api client class that creates the endpoints in the UI to list and generate deployment keys. 

- In the CHIM UI, under the Settings tab that holds the pages in which can create API access keys, I updated the way a user can choose which access key they are requesting. Using radio buttons I was able to set up a dynamic way for a user to choose which access key that they need. 

- Once a key, is created, the user will receive a message that indicates that the key has been created successfully. I created logic on the UI that will show a list keys based on what type of key it is, allows the user to eidt the owners of the key. The keys are then displayed in a table that lists all of the keys that a user has created for each API. The type of access key is shown under a row called "Type".

This project was very challenging to complete, being a novice at React, this project challenged me to learn more and adapt quickly. It gave an in-depth understanding of project planning and agile programming. I was able to contribute to the planning process and my team encouraged me to try things that I have never done before. Working on this project boosted my confidence with React. 

## JIRA Ticket Completions and other team contributions

Throughout the time that I have been on Team THOR and working on the CHIM project, I have compelted various JIRA tickets that range from bug fixes, to epics for new projects, and overall improvements that need to be made to CHIM. Here are some other contributions that I have made to the CHIM tool: 


- Implementing bug fixes, such as updating validations to require specific information during the incident creating process

- Created E2E testing for logout and contact pages in CHIM, E2E tests on contacts page test to make sure that the on-call user can be paged on the contacts page in CHIM. E2E tess for logout page make sure that the logout buttons work when clicked on. 

- Assist internal customers in real time in the use of CHIM and all of its features, specifically US customers as our team in primarily based in the EU and India

- Perform code reviews on incoming PRs and implemented styling fixes on various aspects of CHIM, such as updating the name of specific metrics to measure how long it took to restore service 

- Implemented fixed to update validation for change notice workflow to apply a minimum character count to ensure all required information is being filled out 

- Made updates to filtering in CHIM so that when a user is searching for a specific incident or change notice that data is returned filtered based on the parameters entered in by the user 

- Fixed bug that caused incorrect time to display when an incident is resolved, fixed timing so that the time to notify a user of an outage starts after an incident is reported 

### Testimonials

During my on-the-job training, I had the opportunity to work and collaborate with a very talented group of engineers and IT professionals. Below are some reflections from my teammates about our time working together. 
<br>

> <p>I work as a Technical Leader with the Thor Tooling team, which Krystal is a member of. I have worked on a number of small items with Krystal over the last 8 months on both the CHIM tool and SLO dashboard. Krystal has always been a fast learner, she asks the right questions to ensure she understands the tasks and is very adaptable. Her focus on customer service is very strong and she is willing to help customers even when she was still very new to the team and the projects we were working on. Krystal is punctual, contactable, and always pleasant to work with. She has made a number of solid contributions to the CHIM project that have helped the Tool to progess and meet our customers needs. I was also impressed with the presentation skills that Krystal showed for her Front-End Module project. I look forward to continuing to work with Krystal in the future. - <b><i> Noel Healy, Technical Leader at Cisco Systems, Inc. </i></b>
 
</p>