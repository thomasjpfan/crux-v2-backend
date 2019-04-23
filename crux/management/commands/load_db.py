from django.core.management.base import BaseCommand

from crux.models import User
from crux.models import Dataset
from crux.models import DatasetTag
from crux.models import Task
from crux.models import Analysis
from crux.models import AnalysisTag


class Command(BaseCommand):
    help = 'Initializes database with data'

    def handle(self, *args, **options):

        User.objects.all().delete()
        Dataset.objects.all().delete()
        DatasetTag.objects.all().delete()
        Task.objects.all().delete()
        Analysis.objects.all().delete()
        AnalysisTag.objects.all().delete()

        user = User.objects.create_superuser(
            'thomasjpfan', 'thomas.fan@columbia.com', 'scikit-learn')

        datasets = [
            ({
                'name':
                'Willingness to pay for Hepatitis B vaccination in Selangor, Malaysia',
                'description':
                r'The aim of this study was to investigate the determinants of willingness to pay (WTP) for adult HepB vaccines in Selangor, Malaysia. WTP for hepatitis B (HepB) vaccine was estimated using the Contingent Valuation Method, and factors affecting WTP were modeled with logit regression.',
                'created_by': user,
                'figshare_id': 7559771,
            }, ['Health Economics']),
            ({
                'name':
                'Influence of sports flooring and shoes on impact forces and performance during jump tasks',
                'description':
                r'We aim to determine the influence of sports floorings and sports shoes on impact mechanics and performance during standardised jump tasks. Twenty-one male volunteers performed ankle jumps (four consecutive maximal bounds with very dynamic ankle movements) and multi-jumps (two consecutive maximal counter-movement jumps) on force plates using minimalist and cushioned shoes under 5 sports flooring (SF) conditions. The shock absorption properties of the SF, defined as the proportion of peak impact force absorbed by the tested flooring when compared with a concrete hard surface, were: SF0 = 0% (no flooring), SF1 = 19%, SF2 = 26%, SF3 = 37% and SF4 = 45%. Shoe and flooring effects were compared using 2x5 repeated-measures ANOVA with post-hoc Bonferroni-corrected comparisons. A significant interaction between SF and shoe conditions was found for VILR only (p = 0.003). In minimalist shoes, SF influenced Vertical Instantaneous Loading Rate (VILR) during ankle jumps (p = 0.006) and multi-jumps (p<0.001), in accordance with shock absorption properties. However, in cushioned shoes, SF influenced VILR during ankle jumps only (p<0.001). Contact Time was the only additional variable affected by SF, but only during multi-jumps in minimalist shoes (p = 0.037). Cushioned shoes induced lower VILR (p<0.001) and lower Contact Time (p≤0.002) during ankle jumps and multi-jumps compared to minimalist shoes. During ankle jumps, cushioned shoes induced greater Peak Vertical Ground Reaction Force (PVGRF, p = 0.002), greater Vertical Average Loading Rate (p<0.001), and lower eccentric (p = 0.008) and concentric (p = 0.004) work. During multi-jumps, PVGRF was lower (p<0.001) and jump height was higher (p<0.001) in cushioned compared to minimalist shoes. In conclusion, cushioning influenced impact forces during standardised jump tasks, whether it was provided by the shoes or the sports flooring. VILR is the variable that was the most affected.',
                'created_by': user,
                'figshare_id': 5491138
            }, [
                'Biophysics', 'Space Science', 'Medicine', 'Neuroscience',
                'Physiology', 'Biotechnology', 'Evolutionary Biology',
                'Chemical Sciences', 'Sociology', 'Biological Sciences',
                'Developmental Biology'
            ]),
            ({
                'name': 'Top 100 Government Domain',
                'description':
                r'From a national security viewpoint, a higher degree of cyber autonomy is crucial to reduce the reliance on external, often times uncertain and untrustworthy entities, achieving better resilience against adversaries. To probe into the concept of cyber autonomy of governments, this study examines the external dependency of the public-facing government websites across the world’s major industrialized, Group of Seven (G7) countries. With a further investigation on the web re-sources loaded by G7 government sites, we find that approximately85% of them originate from the United States. By reviewing policy documents and surveying technicians who maintain government websites, we identify three significant forces that can influence the degree of a government’s autonomy, including government mandates on HTTPS adoption, website development outsourcing, and the citizen’s fear of large-scale surveillance. Because a government website is considered as a nation’s critical information infrastructure, we expect this study to raise awareness of their complex dependency, thereby reducing the risk of blindly trusting external entities when using critical government services.new messages',
                'created_by': user,
                'figshare_id': 7301459
            }, [
                'Networking and Communications',
                'Web Technologies (excl. Web Search)',
                'Policy and Administration'
            ]),
            ({
                'name':
                'Neighborhood characteristics and violence behind closed doors: The spatial overlap of child maltreatment and intimate partner violence',
                'description':
                r'In this study, we analyze first whether there is a common spatial distribution of child maltreatment (CM) and intimate partner violence (IPV), and second, whether the risks of CM and IPV are influenced by the same neighborhood characteristics, and if these risks spatially overlap. To this end we used geocoded data of CM referrals (N = 588) and IPV incidents (N = 1450) in the city of Valencia (Spain). As neighborhood proxies, we used 552 census block groups. Neighborhood characteristics analyzed at the aggregated level (census block groups) were: Neighborhood concentrated disadvantage (neighborhood economic status, neighborhood education level, and policing activity), immigrant concentration, and residential instability. A Bayesian joint modeling approach was used to examine the spatial distribution of CM and IPV, and a Bayesian random-effects modeling approach was used to analyze the influence of neighborhood-level characteristics on small-area variations of CM and IPV risks. For CM, 98% of the total between-area variation in risk was captured by a shared spatial component, while for IPV the shared component was 77%. The risks of CM and IPV were higher in neighborhoods characterized by lower levels of economic status and education, and higher levels of policing activity, immigrant concentration, and residential instability. The correlation between the log relative risk of CM and IPV was .85. Most census block groups had either low or high risks in both outcomes (with only 10.5% of the areas with mismatched risks). These results show that certain neighborhood characteristics are associated with an increase in the risk of family violence, regardless of whether this violence is against children or against intimate partners. Identifying these high-risk areas can inform a more integrated community-level response to both types of family violence. Future research should consider a community-level approach to address both types of family violence, as opposed to individual-level intervention addressing each type of violence separately.',
                'created_by': user,
                'figshare_id': 6457451
            }, [
                'Medicine', 'Biotechnology', 'Environmental Sciences',
                'Sociology', 'Biological Sciences', 'Mathematical Sciences',
                'Plant Biology'
            ]),
            ({
                'name':
                'Credit card risk behavior on college campuses: evidence from Brazil',
                'description':
                r"This data set support the following research: College students frequently show they have little skill when it comes to using a credit card in a responsible manner. This article deals with this issue in an emerging market and in a pioneering manner. University students (n = 769) in São Paulo, Brazil's main financial center, replied to a questionnaire about their credit card use habits. Using Logit models, associations were discovered between personal characteristics and credit card use habits that involve financially risky behavior. The main results were: (a) a larger number of credit cards increases the probability of risky behavior; (b) students who alleged they knew what interest rates the card administrators were charging were less inclined to engage in risky behavior. The results are of interest to the financial industry, to university managers and to policy makers. This article points to the advisability, indeed necessity, of providing students with information about the use of financial products (notably credit cards) bearing in mind the high interest rates which their users are charged. The findings regarding student behavior in the use of credit cards in emerging economies are both significant and relevant. Furthermore, financial literature, while recognizing the importance of the topic, has not significantly examined the phenomenon in emerging economies.",
                'created_by': user,
                'figshare_id': 6735383
            }, ['Ecology', 'Science Policy']),
            ({
                'name': 'MHC-linked microsatellite genotypes',
                'description':
                r"This data file contains genotypes for 14 microsatellite markers linked to major histocompatibility complex (MHC) genes that were genotyped in 105 coyotes (Canis latrans) sampled in New York, New Jersey, and Connecticut. Metadata includes sample identification number and urbanization subgroup. The two subgroups include coyotes sampled within New York City (NYC) and outside of NYC (non-NYC). Please see the map provided in Figure 1 to better visualize sampling locations. Missing genotype data is indicated with zeros.",
                'created_by': user,
                'figshare_id': 7704791
            }, [
                'Genetics', 'Environmental Sciences', 'Chemical Sciences',
                'Ecology', 'Immunology', 'Biological Sciences'
            ]),
            ({
                'name': 'StableisotopeDATA',
                'description':
                r"This dataset includes stables isotope values of carbon and nitrogen measured from ants and other arthropods in New York City. It indicates the sample ID, the sample location (lat/long), and stable isotope ratios.",
                'created_by': user,
                'figshare_id': 4081764
            }, [
                'Microbiology', 'Evolutionary Biology',
                'Environmental Sciences', 'Chemical Sciences', 'Ecology',
                'Mathematical Sciences', 'Computational Biology'
            ]),
        ]

        datasets_objs = []
        for (ds_kwargs, tags) in datasets:
            ds, _ = Dataset.objects.get_or_create(**ds_kwargs)
            datasets_objs.append(ds)

            for tag_name in tags:
                tag, _ = DatasetTag.objects.get_or_create(pk=tag_name)
                ds.tags.add(tag)

        t1, _ = Task.objects.get_or_create(
            name="Feature agglomeration",
            dataset=datasets_objs[0],
            created_by=user)

        t2, _ = Task.objects.get_or_create(
            name="Clean data", dataset=datasets_objs[1], created_by=user)

        for ds_obj in datasets_objs:
            Task.objects.get_or_create(
                name="Explore data", created_by=user, dataset=ds_obj)

        explore_tag, _ = AnalysisTag.objects.get_or_create(pk="explore")
        clean_tag, _ = AnalysisTag.objects.get_or_create(pk="cluster")

        a1, _ = Analysis.objects.get_or_create(
            name=
            "PyCellBase, an efficient python package for easy retrieval of biological data from heterogeneous sources",
            description=
            "PyCellBase use case. Example of usage of the PyCellBase REST client library. (IPYNB 15 kb)",
            figshare_id=7915535,
            dataset=datasets_objs[0],
            created_by=user,
            task=t1)
        a1.tags.add(explore_tag)

        a2, _ = Analysis.objects.get_or_create(
            name=
            "DILS 2018 paper on research infrastructures that curate scientific information",
            description=
            r"The Jupyter notebook is supplementary material to Stocker et al. (2018) \"Towards research infrastructures that curate scientific information: A use case in life sciences\" originally submitted to the Data Integration in the Life Sciences (DILS 2018) conference, November 20-21, Hannover, Germany.",
            figshare_id=6874763,
            dataset=datasets_objs[1],
            created_by=user,
            task=t1)
        a2.tags.add(clean_tag, explore_tag)
