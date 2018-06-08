import React from "react";
import Layout from "../layouts/Layout";
import Header from "../ui/brand/Header";
import Benefices from "./HomepageBenefices";
import CommentCaMarche from "./HomepageCommentCaMarche";
import Chronophage from "./HomepageChronophage";
import graphcms from "../../lib/graphcms";

class HomePage extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      Pagedaccueil: {}
    };
  }
  componentWillMount() {
    const query = `{
      Pagedaccueil(id:"cjfdxk4tpcy3v016424h68se6") {
        commentcamarchetitre
        commentcamarchebloc1
        commentcamarchebloc2
        commentcamarchebloc3
        commentcamarchebloc1titre
        commentcamarchebloc2titre
        commentcamarchebloc3titre
        header
        headercalltoaction
        headertitre
        probleme
        benefices
        texteduformulaireaideecoquartiers
        texteduformulairedecontact
      }
    }
    `;
    graphcms.request(query).then(Pagedaccueil => {
      this.setState(Pagedaccueil);
    });
  }
  render() {
    const content = this.state.Pagedaccueil;
    return (
      <Layout>
        <Header
          title={content.headertitre}
          subtitle={
            <div dangerouslySetInnerHTML={{ __html: content.header }} />
          }
          callToActionText={content.headercalltoaction}
        />
        <CommentCaMarche data={content} />
        <Chronophage data={content} />
        <Benefices data={content} />
      </Layout>
    );
  }
}

export default HomePage;