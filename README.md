#Slack-VC
Slack-VC is a Slack integration to look up famous Venture Capital's portfolio list. It's built for startup enthusiasts! 😇
![Example](http://g.recordit.co/VjMbZJevur.gif)

## Coverage
Currently, the VCs supported and corresponding commands:

- [a16z](http://a16z.com/): /vc a16z p
- [Khosla Ventures](http://www.khoslaventures.com/): /vc khosla p
- [Sequoia Capital](https://www.sequoiacap.com/): /vc sequoia p
- [KPCB](http://www.kpcb.com/): /vc kpcb p
- [Founders Fund](http://foundersfund.com/): /vc ff p
- [GreyLock Partners](http://www.greylock.com/): /vc greylock p

## Integrate with your Slack

1. Go to one of your Slack channel.
2. Click the **Channel Settings**.
3. In the settings menu, click the **Add an app or integration**.
4. In the top menu bar, click **Manage**, then click the **Custom Integrations** on the left menu bar.
5. Click **Slash Commands**.
6. Click **Add Configuration**.

- Command: /vc
- URL: https://slack-vc.herokuapp.com/
- Method: **POST**
- In the Autocomplete help text section, check to allow autocomplete.
  - Description: VC's portfolio list, articles is in Slack now!
  - Usage hint: [VC name +  Space + Option]
7. All set!
