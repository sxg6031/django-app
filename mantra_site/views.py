from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Cover, Tiles, Section2, Videos, About

# Create your views here.


class MainView(TemplateView):
    template_name = 'index.html'


    def get_context_data(self, *args, **kwargs):
        context = super(MainView, self).get_context_data(*args, **kwargs)

        # cover image
        context["cover_image"] = Cover.objects.get(id=1).cover_image
        # end

        # Tiles view
        context["heading"] = Tiles.objects.get(id=1).heading

        context["image1"] = Tiles.objects.get(id=1).image1
        context["image1_heading"] = Tiles.objects.get(id=1).image1_heading
        context["image1_para"] = Tiles.objects.get(id=1).image1_para

        context["image2"] = Tiles.objects.get(id=1).image2
        context["image2_heading"] = Tiles.objects.get(id=1).image2_heading
        context["image2_para"] = Tiles.objects.get(id=1).image2_para

        context["image3"] = Tiles.objects.get(id=1).image3
        context["image3_heading"] = Tiles.objects.get(id=1).image3_heading
        context["image3_para"] = Tiles.objects.get(id=1).image3_para

        context["image4"] = Tiles.objects.get(id=1).image4
        context["image4_heading"] = Tiles.objects.get(id=1).image4_heading
        context["image4_para"] = Tiles.objects.get(id=1).image4_para

        context["image5"] = Tiles.objects.get(id=1).image5
        context["image5_heading"] = Tiles.objects.get(id=1).image5_heading
        context["image5_para"] = Tiles.objects.get(id=1).image5_para

        context["image6"] = Tiles.objects.get(id=1).image6
        context["image6_heading"] = Tiles.objects.get(id=1).image6_heading
        context["image6_para"] = Tiles.objects.get(id=1).image6_para
        # end

        # ======== section2 =========== #
        context["sec2_heading"] = Section2.objects.get(id=1).sec2_heading
        context["sec2_image1"] = Section2.objects.get(id=1).sec2_image1
        context["sec2_image2"] = Section2.objects.get(id=1).sec2_image2
        # =========== end ============== #

        # ========== Videos View
        context["video1"] = Videos.objects.get(id=1).video1
        context["video1_heading"] = Videos.objects.get(id=1).video1_heading
        context["video1_para"] = Videos.objects.get(id=1).video1_para

        context["video2"] = Videos.objects.get(id=1).video2
        context["video2_heading"] = Videos.objects.get(id=1).video2_heading
        context["video2_para"] = Videos.objects.get(id=1).video2_para

        context["video3"] = Videos.objects.get(id=1).video3
        context["video3_heading"] = Videos.objects.get(id=1).video3_heading
        context["video3_para"] = Videos.objects.get(id=1).video3_para
        # ========== end

        # ============ About View ============ #
        context["profile_picture"] = About.objects.get(id=1).profile_picture
        context["profile_para"] = About.objects.get(id=1).profile_para
        context["my_map"] = About.objects.get(id=1).my_map
        context["address"] = About.objects.get(id=1).address
        context["phone"] = About.objects.get(id=1).phone
        context["email"] = About.objects.get(id=1).email
        context["facebook"] = About.objects.get(id=1).facebook
        context["youtube"] = About.objects.get(id=1).youtube
        # ============ end ============= #

        return context
