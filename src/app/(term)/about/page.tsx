import Image from "next/image";
import React from "react";
import color_hunt_logo_animation_gif from "@/app/photos/color-hunt-logo-animation.gif";

export default function About() {
  return (
    <div
      className={`flex flex-col justify-center items-center gap-10 *:*:p-2 px-5`}
    >
      <Image
        src={color_hunt_logo_animation_gif}
        alt={`color-hunt-logo-animation.gif`}
        className={`w-52  object-cover`}
      />
      <div>
        <h1 className={`text-center font-bold`}>Color Hunt</h1>
        <p>
          Color Hunt is an open collection of beautiful color palettes, created
          by Gal Shir. Color Hunt started as a personal small project built to
          share trendy color combinations between a group of designer friends.
          The collection scaled up and now being used daily as a handy resources
          by thousands of people all over the world. Color Hunt was created with
          the goal of celebrating the beauty of colors, and to serve as a go-to
          resource for color inspiration.
        </p>
      </div>
      <div>
        <h1 className={`text-center font-bold`}>Who creates the color palettes?</h1>
        <p>
          You, the users, are the ones who create the palettes using Color
          Hunt’s palette creator. The collection is open, and everyone can
          create and submit their own color combination. That’s how we keep
          Color Hunt diverse, colorful, social and inspiring. Each palette is a
          public property and not owned by a specific creator, nor by Color
          Hunt.
        </p>
      </div>
      <div>
        <h1 className={`text-center font-bold`}>Which palettes get featured?</h1>
        <p>
          Color Hunt is open, but is also curated. It means that all the
          palettes are hand-picked by Color Hunt’s curators. Each submission of
          a color palette is being reviewed to make sure it fits the
          collection’s goals. Each day, the very best submission is being picked
          up and will be visible on the homepage in the day after.
        </p>
      </div>
      <div>
        <h1 className={`text-center font-bold`}>Made by Gal Shir</h1>
        <p>
          Color Hunt was founded by Gal Shir, designer and artist from Tel Aviv
          who is passioned about colors. Gal runs Color Hunt since 2015 with the
          goal of sharing that passion with the world, and provide a handy
          resource for designers and artists.
        </p>
      </div>
      <div>
        <h1 className={`text-center font-bold`}>Partnerships/sponsorships</h1>
        <p>Reach out to hello@galshir.com</p>
      </div>
    </div>
  );
}
